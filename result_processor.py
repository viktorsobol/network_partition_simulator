import mysql.connector

file_equal_experiment = open('eq_mean_experiment.txt', 'r')

batch_size = 100

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="network_partition_modeling"
)

mycursor = mydb.cursor()

sql = "INSERT INTO eq_mean_experiment (g_number, m_up, m_down, epoch_lenght, res) VALUES (%s, %s, %s, %s, %s)"
val = []
total = 0
current_batch_size = 0
for line in file_equal_experiment:
    current_batch_size += 1
    values = tuple(map(int, map(lambda l: l[1], map(lambda l: l.split('='), line.split(',') ))))
    val.append(values)
    total += 1
    if len(val) >= batch_size:
        print(val)
        mycursor.executemany(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "was inserted.")
        val = []
        current_batch_size = 0

mycursor.executemany(sql, val)
mydb.commit()
print("Total records was inserted - {}".format(total))



