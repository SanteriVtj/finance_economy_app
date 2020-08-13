$('select').change(function() {
    alert($('#first_cat').val());
});

$('select').change(function() {
    $.ajax({
            url: "/graph",
            type: "GET",
            contentType: 'application/json;charset=UTF-8',
            data: {
                'selected': document.getElementById('first_cat').value
    
            },
            dataType:"json",
            success: function (data) {
                Plotly.newPlot(document.getElementById('graph'), data);
            },
            timeout: 500000
        });
});