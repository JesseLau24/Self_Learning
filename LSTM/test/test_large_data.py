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
    # 创建一个大型数据集
    def generate_data():
        while True:
            yield (tf.random.uniform(shape=(1000, 64)), 
                   tf.random.uniform(shape=(1000, 1)))
    
    dataset = tf.data.Dataset.from_generator(generate_data, 
                                             (tf.float32, tf.float32), 
                                             (tf.TensorShape([1000, 64]), 
                                              tf.TensorShape([1000, 1])))
    dataset = dataset.batch(32).prefetch(tf.data.AUTOTUNE)

    # 定义一个更复杂的模型
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(1000, 64)),  # 更新输入形状
        tf.keras.layers.LSTM(128, return_sequences=True),
        tf.keras.layers.LSTM(128),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    print("TensorFlow is installed and running correctly.")
    
    # 训练模型
    model.fit(dataset, epochs=3, steps_per_epoch=100)

except Exception as e:
    print(f"An error occurred: {e}")

# 检查 TensorFlow 是否可以使用 GPU
if tf.config.list_physical_devices('GPU'):
    print("TensorFlow is using GPU.")
else:
    print("TensorFlow is using CPU.")

# 结束计时
end_time = time.time()

# 输出耗时
print(f"Elapsed time: {end_time - start_time:.2f} seconds")
