import tensorflow as tf
import time

# 开始计时
start_time = time.time()

# 打印 TensorFlow 版本
print(f"TensorFlow version: {tf.__version__}")

# 检查 TensorFlow 是否可以使用 GPU
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# 确认 TensorFlow 是否能正常运行
try:
    # 使用 Input(shape) 定义输入层
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(100, 64)),  # 增加输入形状
        tf.keras.layers.LSTM(128, return_sequences=True),
        tf.keras.layers.LSTM(128, return_sequences=True),
        tf.keras.layers.LSTM(128),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    print("TensorFlow is installed and running correctly.")
except Exception as e:
    print(f"An error occurred: {e}")

# 检查 TensorFlow 是否可以使用 GPU
if tf.config.list_physical_devices('GPU'):
    print("TensorFlow is using GPU.")
else:
    print("TensorFlow is using CPU.")

# 显示设备列表
print("Devices available:")
for device in tf.config.list_physical_devices():
    print(device)

# 创建一个更复杂的张量运算以确认计算设备
print("\nTesting a more complex tensor operation:")
a = tf.random.uniform(shape=(1000, 64))
b = tf.random.uniform(shape=(64, 1000))
c = tf.matmul(a, b)

print("Result of matrix multiplication:")
print(c.numpy())

# 结束计时
end_time = time.time()

# 输出耗时
print(f"Elapsed time: {end_time - start_time:.2f} seconds")
