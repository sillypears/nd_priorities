$(function() {
    $.getJSON('necrodancer.json', function(data) {
        var content = "<table id=\"enemies\" class=\"table table-bordered\">";
        const width = $(document).width()
        const total = data.length
        const rows =  Math.floor(width/total)+1
        $.each(data, function(e) {
            if ((e%rows) == 0 ||  e == 0) {
                content += "<tr>";
            }
            let ttip = "Name: " + data[e]["name"] + "<br />Type: " + data[e]["type"] + "<br />Priority: " + data[e]["priority"];
            content += "<td class=\"text-center\">" + data[e]["priority"] + "\n<img data-html=\"true\" data-toggle=\"tooltip\" title=\"" + ttip + "\" src=\"" + data[e]['sprite'] + "\"></td>"

            if ( (e+1%rows) == 0 && e != 0) {
                content += "</tr>"
            }
        });
       content += "</tr></table>"
       $('div#content').html(content)
       $('[data-toggle="tooltip"]').tooltip();
    });
});