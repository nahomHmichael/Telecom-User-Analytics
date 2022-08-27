def convert_bytes_to_megabytes(df, bytes_data):
    megabyte = 1*10e+5
    df[bytes_data] = df[bytes_data] / megabyte
    
    return df[bytes_data]