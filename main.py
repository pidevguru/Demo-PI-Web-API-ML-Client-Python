from piwebapiml.pml_web_api_client import PMLWebApiClient


def main():
    client = PMLWebApiClient("https://marc-pi2018.marc.net/piwebapi", False)
    client.set_basic_auth("marc.adm", "1")
    pi_point = client.get_pi_point("\\\\MARC-PI2018\\sinusoid")
    pi_point2 = client.get_pi_point("\\\\MARC-PI2018\\sinusoidu")
    pi_point3 = client.get_pi_point("\\\\MARC-PI2018\\cdt158")        
    attr = client.get_af_attribute('\\\\MARC-PI2018\\Weather\\Cities\\Chicago|Pressure')
        
    df1 = pi_point.get_recorded_values(start_time="*-1d", end_time="*")
    df2 = pi_point.get_recorded_values(start_time="*-1d", end_time="*",
                                          selected_fields="items.value;items.timestamp")
      

if __name__ == "__main__":
    main()