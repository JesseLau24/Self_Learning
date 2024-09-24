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
    # 使用更大规模的张量进行运算
    a = tf.random.uniform(shape=(10000, 1000))
    b = tf.random.uniform(shape=(1000, 10000))
    c = tf.matmul(a, b)

    print("Result of matrix multiplication:")
    print(c.numpy())

    print("TensorFlow is installed and running correctly.")
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
