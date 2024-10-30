import tensorflow as tf

def create_placeholder_model():
    # Define a simple placeholder model
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=(10,)),  # Use input_shape instead of batch_shape
        tf.keras.layers.Dense(1)  # Simple output layer
    ])
    
    # Compile the model
    model.compile(optimizer='adam', loss='mse')
    
    # Save the model
    model.save("app/models/engagement_model.h5")
    print("Placeholder model created and saved as app/models/engagement_model.h5")

if __name__ == "__main__":
    create_placeholder_model()

