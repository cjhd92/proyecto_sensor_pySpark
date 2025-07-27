

def read_sensor_data(SpSession,ubicacion):
    df = SpSession.read.csv(ubicacion,header=True,inferSchema = True)
    return df