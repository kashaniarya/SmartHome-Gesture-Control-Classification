package com.example.ayan.firstandroidcode;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.widget.Toast;

public class serviceEx extends Service {
    public serviceEx() {
    }
    @Override
    public void onCreate(){
        //sendMessageToMainActivity();
    }
    @Override
    public IBinder onBind(Intent intent) {
        // TODO: Return the communication channel to the service.
        sendMessageToMainActivity();
        //throw new UnsupportedOperationException("Not yet implemented");
        return null;
    }

    public void sendMessageToMainActivity(){
        for (int i = 0; i < 10; i++){
            Toast.makeText(this, "No: " + i, Toast.LENGTH_SHORT).show();
        }
    }
}
