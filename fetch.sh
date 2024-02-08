#!/bin/bash

rm $(/usr/bin/grep "error.http.500" -l -R . | grep -v "fetch.sh")
rm $(/usr/bin/grep "upstream connect error or disconnect/reset" -l -R . | grep -v "fetch.sh")
rm $(/usr/bin/grep "The proxy server could not handle the request<p>Reason: <strong>Error" -l -R . | grep -v "fetch.sh")
rm $(/usr/bin/grep "no healthy upstream" -l -R . | grep -v "fetch.sh")
find . -type f -empty -delete
errorCount=0

for category in goods works service;
do
  for id in {1..250000};
  do
    if [ ! -f "raw/${category}/${id}.json" ]; then
      echo "${category}: ${id} (Error Count: ${errorCount})"
      if [ $errorCount -ge 200 ]; then
        break
      fi
      curl "https://kppp.karnataka.gov.in/supplier-registration-service/v1/api/portal-service/${id}/${category}-tender-full-view" -H 'Accept: application/json, text/plain, */*' -H 'Post: CONTRACTOR-EPROC-CONTRACTOR' -H 'Connection: keep-alive' -H 'Referer: https://kppp.karnataka.gov.in/' > "raw/${category}/${id}.json"
      sleep 1
      if /usr/bin/grep "error.http.500" "raw/${category}/${id}.json"; then
        ((errorCount++))
        continue
      fi
      if /usr/bin/grep "upstream connect error or disconnect/reset" "raw/${category}/${id}.json"; then
        continue
      fi
      errorCount=0
    else
      errorCount=0
    fi
  done
done

rm $(/usr/bin/grep "error.http.500" -l -R . | grep -v "fetch.sh")
rm $(/usr/bin/grep "upstream connect error or disconnect/reset" -l -R . | grep -v "fetch.sh")
rm $(/usr/bin/grep "The proxy server could not handle the request<p>Reason: <strong>Error" -l -R . | grep -v "fetch.sh")
rm $(/usr/bin/grep "no healthy upstream" -l -R . | grep -v "fetch.sh")
find . -type f -empty -delete
