package edu.asu.impact.cse535_example1;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;


/**
 * Created by Administrator on 2016-01-13.
 */
public class SecondActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activty_second);
        Button btn2 = (Button) findViewById(R.id.button);
        btn2.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent previousPage = new Intent(SecondActivity.this, MainActivity.class);
                startActivity(previousPage);
            }
        });
    }
}
