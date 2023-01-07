//เราจะใช้ 2 Library นั้นก็คือ NumpyและPandas
import pandas as pd
import numpy as np
//เตรียมไฟล์//
pd.read_CSV('ไฟล์ข้อมูลของเรา')

//ให้แสดงข้อมูลทุกแถว//
pd.set_option('display.max_rows',none)

//จากนั้นลบข้อมูล//
df=df.dropna(subset=['ข้อลัมน์ที่มีข้อมูลขยะ']).reset_index(drop=true)
df

//เพื่อประหยัดเวลาในการไม่ต้องเปิดชื่อคอลัมน์ทั้งหมดและแก้ไขลำดับคอลัมน์//
df.columns
df[['คอลัมน์1,คอลัมน์2,คอลัมน์3,คอลัมน์4,คอลัมน์5,คอลัมน์6,คอลัมน์7,คอลัมน์8,คอลัมน์9,]].to_CSV('ชื่อไฟล์', index = false


