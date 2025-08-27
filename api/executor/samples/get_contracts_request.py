from api.endpoints.customer.customer_web import get_contracts


response = get_contracts()
print(response.status_code)
