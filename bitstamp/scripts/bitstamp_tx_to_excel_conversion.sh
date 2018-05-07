#!/bin/bash

BS_TX_FILE=$1

if [ ! -f "$BS_TX_FILE" ] ; then
  >&2 echo "FATAL - file not found \"$BS_TX_FILE\", please specify the input file"
  exit -1
fi

DEBUG=true
HEADER="Type,Datetime,Account,Amount,Amount_CT,Value,Value_CT,Rate,Rate_CT,Fee,Fee_CT,Sub Type"

echo $HEADER

SKIP_HEADER=x
tmpIFS=$IFS
IFS=$'\n'
while read -r line
do
  if [ $SKIP_HEADER = "x" ] ; then
    SKIP_HEADER=$line
    continue
  fi
  n=$(echo $line)
  lead_content=$(echo $n | cut -d, -f1-5)
  amount=$(echo $n | cut -d, -f6)
  value=$(echo $n | cut -d, -f7)
  rate=$(echo $n | cut -d, -f8)
  fee=$(echo $n | cut -d, -f9)
  trail_content=$(echo $n | cut -d, -f10-)
  if [ $DEBUG = "true" ] ; then
    if [ "$line" != "$lead_content,$amount,$value,$rate,$fee,$trail_content" ] ; then
      >&2 echo "ERROR - parsed incorrectly > $line to $lead_content,$amount,$value,$rate,$fee,$trail_content"
    fi
  fi
  amount_ct=$(echo $amount | cut -d" " -f2-)
  value_ct=$(echo $value | cut -d" " -f2-)
  rate_ct=$(echo $rate | cut -d" " -f2-)
  fee_ct=$(echo $fee | cut -d" " -f2-)
  amount=$(echo $amount | cut -d" " -f1)
  value=$(echo $value | cut -d" " -f1)
  rate=$(echo $rate | cut -d" " -f1)
  fee=$(echo $fee | cut -d" " -f1)
  echo "$lead_content,$amount,$amount_ct,$value,$value_ct,$rate,$rate_ct,$fee,$fee_ct,$trail_content"
done <"$BS_TX_FILE"

IFS=$tmpIFS

exit 0
