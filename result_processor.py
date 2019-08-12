import mysql.connector

file_equal_experiment = open('AWS_eq_mean_experiment.txt', 'r')
file_NOT_equal_experiment = open('AWS_NOT_eq_mean_experiment.txt', 'r')

batch_size = 100

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="network_partition_modeling"
)

mycursor = mydb.cursor()
sql = "INSERT INTO experiment_results (node_number, g_number, m_up, m_down, epoch_lenght, result, all_node_means_equal) VALUES (%s, %s, %s, %s, %s, %s, %s)"


def insert_experiment_results_to_db(result_file, equal_node_means: bool, node_number: int):
  val = []
  total = 0
  current_batch_size = 0
  for line in result_file:
      current_batch_size += 1
      values = tuple(map(int, map(lambda l: l[1], map(lambda l: l.split('='), line.split(',')[1:] ))))
      values = (node_number, ) + values + (equal_node_means,)
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



insert_experiment_results_to_db(file_equal_experiment, True, 5)
insert_experiment_results_to_db(file_NOT_equal_experiment, False, 5)




