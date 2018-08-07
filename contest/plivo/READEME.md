Message API:

Use a created plivo account for all api firing.
Details of account are :
Auth id : MAODUZYTQ0Y2FMYJBLOW
Auth token : Mzk0MzU1Mzc3MTc1MTEyMGU2M2RlYTIwN2UyMzk1

Please use python and/or its any test framework 
Please use modular coding to do the same.
Once done, please host the code on your public repo on github

Before Start :
All plivo api docs could be found here
All plivo api should be authenticated.Details could be found here

Scenarios :
1. Use any two numbers available in the account.Get all numbers api to find any two numbers. 
2. Use message api to send an sms from a number to another number.One can use both number bought as above to do this.
3. Once message api is successful, response give message uuid.Using this message uuid get the details of the message using details api.
4. Use pricing api to determine the rate of the message which is outbound rate under message object in this case.
Sample response for this looks like :

	"message": {
        	"inbound": {
            	"rate": "0.00000"
    },
 "outbound": {
            	"rate": "0.00650"
              },
           "outbound_networks_list": [
           		 {
                "group_name": "US",
                "rate": "0.00650"
            },
            	{
                "group_name": "US",
                "rate": "0.00650"
            }
        	   ]
},


5. Verify the rate and the price deducted for the sending message, should be same.
6. And finally after sending message, using account details api, account cash credit should be less than by the deducted amount.




