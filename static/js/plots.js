$('#first_cat').on('change' ,function() {
    $.ajax({
            url: "/graph/",
            type: "GET",
            contentType: 'application/json;charset=UTF-8',
            data: {
                'selected': document.getElementById('first_cat').value
    
            },
            beforeSend: function() {
                document.getElementById('spinner').style.display='block';
                document.getElementById('graph').style.display='none';
            },
            dataType:"json",
            success: function (data) {
                console.log(data);
                Plotly.newPlot(document.getElementById('graph'), data);
            },
            timeout: 500000,
            complete: function() {
                document.getElementById('spinner').style.display='none';
                document.getElementById('graph').style.display='block';
            }
        });
});