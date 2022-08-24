def convert_bytes_to_megabytes(df, bytes_data):
    megabyte = 2**10
    df[bytes_data] = df[bytes_data] / megabyte
    
    return df[bytes_data]