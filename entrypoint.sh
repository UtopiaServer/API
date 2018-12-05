#!/bin/bash

if [ "$API_MODE" != "production" ]; then
    parameters=""
else
    parameters="--settings=api.prod_settings"
fi

setup_db() {
    find -type d -name migrations -prune -exec rm -rf {} \;
    find -type d -name __pycache__ -prune -exec rm -rf {} \;
    python manage.py makemigrations ${parameters} `for i in $(ls -d */); do echo ${i%%/}; done | grep -v 'api' | grep -v 'utils'`
    python manage.py migrate ${parameters}
}

load_db_data() {
    if [ ! -f ../backup/`date "+%Y-%m-%d"`.zip ]; then
        new_file=0
    else
        new_file=$(eval 'zipinfo -1 ../backup/`date "+%Y-%m-%d"`.zip | wc -l')
    fi
    python manage.py loaddata ${parameters} ../backup/latest.json
    mv ../backup/latest.json ../backup/latest.${new_file}.json
    zip ../backup/`date "+%Y-%m-%d"`.zip ../backup/latest.${new_file}.json
    rm ../backup/latest.${new_file}.json
}

prep_term() {
    unset term_child_pid
    unset term_kill_needed
    trap 'handle_term' TERM INT
}

handle_term() {
    python manage.py dumpdata --exclude auth.permission --exclude contenttypes ${parameters} -o ../backup/latest.json
    if [ "${term_child_pid}" ]; then
        kill -TERM "${term_child_pid}" 2>/dev/null
    else
        term_kill_needed="yes"
    fi
}

wait_term() {
    term_child_pid=$!
    if [ "${term_kill_needed}" ]; then
        kill -TERM "${term_child_pid}" 2>/dev/null 
    fi
    wait ${term_child_pid}
    trap - TERM INT
    wait ${term_child_pid}
}

setup_db
load_db_data

prep_term
python manage.py runserver ${parameters} --noreload 0.0.0.0:8000 &
wait_term


