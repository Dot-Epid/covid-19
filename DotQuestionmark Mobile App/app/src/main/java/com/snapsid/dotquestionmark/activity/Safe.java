package com.snapsid.dotquestionmark.activity;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebView;

import com.snapsid.dotquestionmark.R;

public class Safe extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_safe);

        WebView wv = findViewById(R.id.webview);
        wv.loadUrl("https://coviddashboard.azurewebsites.net/dashboard");
    }
}
