#!/bin/bash
curl -sI http://52b80f1a41ed.20.hbtn-cod.io | grep -i Content-Length | cut -d" " -f2
