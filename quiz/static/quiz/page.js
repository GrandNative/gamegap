$(document).ready(function(){
        var x = 0;
        var start = new Date;
        setInterval(function() {
                $('#timerrrr').text((new Date - start) / 1000 + " Seconds");
        }, 1000)

        setInterval(function() {
            var start = new Date;
            setInterval(function() {
                $('#timerrrr').text((new Date - start) / 1000 + " Seconds");
            }, 1000);
        //The code you want to execute every 5 seconds
            var formData = new FormData();
            var q_num = $("h4").attr("id");
            var a = "1";
            var next_q_num = parseInt(a, 10) + parseInt(q_num, 10);
            console.log(q_num)
            var answer_id = $('input[name=flexRadioDefault]:checked', '#my_form').val()
            console.log(answer_id)
            formData.append('answer_id', answer_id)
            formData.append('q_num', q_num)
            formData.append('next_q_num', next_q_num)
            formData.append('csrfmiddlewaretoken', CSRF_TOKEN)
            for (var key of formData.entries()) {
                console.log(key[0] + ', ' + key[1]);
            }


            $.ajax({
                type: "POST",
                url: '',
                data: formData,
                enctype: 'multipart/form-data',
                processData: false,
                contentType: false,
                cache: false,
                success: function(data){
                    $('#timerrrr').text(0)
                    if (data.last == 1){
                            window.location.href = "khosh-galdin"
   				    }else{
                            $("h4").attr("id", data.question_id)
                            $("h4").text(data.question_title)
                            $("#1").val(data.answer_1['id'])
                            $("#l1").text(data.answer_1['title'])

                            $("#2").val(data.answer_2['id'])
                            $("#l2").text(data.answer_2['title'])

                            $("#3").val(data.answer_3['id'])
                            $("#l3").text(data.answer_3['title'])

                            $("#4").val(data.answer_4['id'])
                            $("#l4").text(data.answer_4['title'])
   				        }
   				    },

            })
        }, 40000);
})