package com.example.ayan.firstandroidcode;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

public class MyReceiver extends BroadcastReceiver {
    public MyReceiver() {
    }

    @Override
    public void onReceive(Context context, Intent intent) {
        // TODO: This method is called when the BroadcastReceiver is receiving
        // an Intent broadcast.
        //String t = intent.getAction();
        Toast.makeText(context,"intent received:",Toast.LENGTH_LONG).show();
        //throw new UnsupportedOperationException("Not yet implemented");
    }
}
