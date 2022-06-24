#!/bin/bash

curl -X POST http://localhost:5000/api/timeline_post -d 'name=Sally&email=sallylee@wustl.edu&content=random post'

curl http://localhost:5000/api/timeline_post