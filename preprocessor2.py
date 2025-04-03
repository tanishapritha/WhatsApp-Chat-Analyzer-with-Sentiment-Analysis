import re
import pandas as pd

def preprocess(data):
    print("🛠️ Preprocessing started...")

    # Ensure proper UTF-8 decoding
    try:
        data = data.decode("utf-8") if isinstance(data, bytes) else data
    except Exception as e:
        print("❌ Encoding Error:", e)
        return None

    # Ignore encryption notice
    data = "\n".join(data.split("\n")[1:])

    # Print first few lines of data to debug
    print("📄 Sample Data:\n", data[:500])  

    # Regex for timestamps
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    
    messages = re.split(pattern, data)[1:]  # Extract messages
    dates = re.findall(pattern, data)  # Extract timestamps

    print(f"✅ Extracted {len(messages)} messages and {len(dates)} timestamps.")

    if len(messages) == 0:
        print("⚠️ No messages were extracted! Check the chat format.")
        return None

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Convert date safely
    try:
        df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ', errors='coerce')
    except Exception as e:
        print("❌ Date conversion error:", e)
        return None

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)

        if entry[1:]:  # Normal messages
            users.append(entry[1])
            messages.append(entry[2])
        else:  # System notifications (group creation, etc.)
            users.append("system_notification")
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages

    df.drop(columns=['user_message'], inplace=True)

    # Remove system messages & "<Media omitted>"
    df = df[(df['user'] != "system_notification") & (~df['message'].str.contains('<Media omitted>'))]

    if df.empty:
        print("⚠️ All extracted messages were system notifications or media files!")
        return None

    print("✅ Preprocessing completed successfully!")
    return df
