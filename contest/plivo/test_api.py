from client import Client
import json

AUTH_ID = 'MAODUZYTQ0Y2FMYJBLOW'
AUTH_TOKEN = 'Mzk0MzU1Mzc3MTc1MTEyMGU2M2RlYTIwN2UyMzk1'

# private method to parse the json output
def _get_response(response):
    resp_str = json.dumps(response)
    return json.loads(resp_str)

# private method to print the header
def _print_heading(string):
    line = '=' * len(string)
    print("\n" + line)
    print(string)
    print(line)

def test_plivo_api():
    step1 = "Step 1 : authenticate and create the api object"
    _print_heading(step1)
    client = Client(auth_id=AUTH_ID, auth_token=AUTH_TOKEN)
    print("PASS: API authentication is successful")

    step2 = "Step 2 : get the 2 phone numbers"
    _print_heading(step2)
    http_res = client.make_request('GET',path='Number')
    resp_str = json.dumps(http_res)
    resp = json.loads(resp_str)

    assert len(resp['objects']) > 1, "Not enough phone numbers"

    numbers = []
    for i in (0,1):
        numbers.append(resp['objects'][i]['number'])

    print("Numbers: ", numbers)

    step3 = "Step 3: send the  message from one number to other"
    _print_heading(step3)
    # throw exception if both numbers are same as
    # source and destination numbers should not be same
    assert numbers[0] != numbers[1], "source and destination numbers should not be same"

    http_res = client.make_request('POST',path='Message', options={'src':numbers[0], 'dst':numbers[1], 'text':'Test Message'})
    resp = _get_response(http_res)
    message_uuid = resp['message_uuid'][0]
    print("message uuid : ", message_uuid)

    step4 = "Step 4: get the detail of message"
    _print_heading(step4)
    mssg_path = 'Message/' + message_uuid
    http_res = client.make_request('GET',path=mssg_path )
    resp = _get_response(http_res)
    price_deducted = resp['total_amount']
    print("Details of message: ", resp)
    print("price deducted : ", price_deducted)

    step5 = "Step 5 - get the pricing of message"
    _print_heading(step5)
    mssg_path = 'Pricing/' + message_uuid
    http_res = client.make_request('GET',path='Pricing', options={'country_iso' : 'US'})
    resp = _get_response(http_res)

    outbound_rate = resp['message']['outbound']['rate']
    print("outbound rate : ", outbound_rate)

    step6 = "Step 6 - verify the rate and the price deducted for the sending message, should be same"
    _print_heading(step6)
    assert price_deducted == outbound_rate, "rate and the price deducted are not same"
    print("PASS: rate and the price deducted for the sending message are same\n")

    step7 = "Step 7 - check if account cash credit should be less than by the deducted amount"
    _print_heading(step7)
    http_res = client.make_request('GET')
    resp = _get_response(http_res)
    cash_credits = resp['cash_credits']
    print("cash_credits: ", cash_credits)

    step8 = "Step 8 - check if account cash credit should be more than by the deducted amount."
    _print_heading(step8)
    assert price_deducted < cash_credits, "deducted amount is greater than account cash credit"
    print("PASS: account cash credit is more than the deducted amount.\n")

