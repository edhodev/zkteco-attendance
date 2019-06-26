import requests
import schedule
import time
import zk
from zk.base import ZK_helper 
from zk.attendance import Attendance
from mongo import base

client      = base.connect();
database    = base.create_database(client, "im_system")
finger_logs = base.create_collection(database, "finger_logs" )

zklib = zk.ZK("192.168.1.15", 4370)


zklib.connect()

# base.delete_all(finger_logs);
base.sort_collection(finger_logs)

def send_attlog(user, timestamp):
    endpoint  = "http://localhost:8000/api/att"
    data      = { 'user': user,  'timestamp': timestamp }
    r         = requests.post(endpoint, data)

    return r.text

def get_attendance():
    attendances = zklib.get_attendance() 

    for attendance in attendances:
        if base.log_exists(finger_logs, {"uid": format(attendance.uid)}) == 0:
            print (send_attlog(format(attendance.user_id), format(attendance.timestamp)))
            base.insert_one_collection(finger_logs,{"uid" : format(attendance.uid), "user_id": format(attendance.user_id), "timestamp": format(attendance.timestamp)})
            base.show_last(finger_logs)


schedule.every(1).seconds.do(get_attendance)

while True: 
        schedule.run_pending()
        time.sleep(1) 




