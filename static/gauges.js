window.onload = function(){
    
    g1 = new JustGage({
            id: "new_gauge",
            value: 0,
            valueFontColor: "#ffffff",
            min: 0,
            max: 20,
            donut: true,
            gaugeWidthScale: 0.3,
            counter: true,
            title: "New",
            hideInnerShadow: true,
            relativeGaugeSize: true,
        });
    g2 = new JustGage({
            id: "transferred_gauge",
            value: 0,
            valueFontColor: "#ffffff",
            min: 0,
            max: 10,
            donut: true,
            gaugeWidthScale: 0.3,
            counter: true,
            title: "Transferred",
            hideInnerShadow: true,
            relativeGaugeSize: true,
        });
    g3 = new JustGage({
            id: "platinum_gauge",
            value: 0,
            valueFontColor: "#ffffff",
            min: 0,
            max: 5,
            donut: true,
            gaugeWidthScale: 0.3,
            counter: true,
            title: "Platinum",
            hideInnerShadow: true,
            relativeGaugeSize: true,
        });
    g4 = new JustGage({
            id: "premium_gauge",
            value: 0,
            valueFontColor: "#ffffff",
            min: 0,
            max: 10,
            donut: true,
            gaugeWidthScale: 0.3,
            counter: true,
            title: "Premium",
            hideInnerShadow: true,
            relativeGaugeSize: true,
        });
};

setInterval(function() {
        g1.refresh(getRandomInt(0, 20));
        g2.refresh(getRandomInt(0, 10));
        g3.refresh(getRandomInt(0, 5));
        g4.refresh(getRandomInt(0, 7));
      }, 5000); // update the charts every 5 seconds.