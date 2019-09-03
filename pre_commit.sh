#!/usr/bin/env bash
echo "#?" > /tmp/test
black .
echo "#$?" >> /tmp/test
