$('#first_cat').on('click' ,function() {
    $.ajax({
            url: "/graph/",
            type: "GET",
            contentType: 'application/json;charset=UTF-8',
            data: {
                'selected': document.getElementById('first_cat').value
    
            },
            dataType:"json",
            success: function (data) {
                console.log(data);
                Plotly.newPlot(document.getElementById('graph'), data);
            },
            timeout: 500000
        });
});