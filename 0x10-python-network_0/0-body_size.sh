#!/bin/bash
curl -sI $URL | grep -i Content-Length | awk '{print $2}'
