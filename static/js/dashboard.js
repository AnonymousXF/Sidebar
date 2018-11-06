$("#appendSingleHost > div > div > div.modal-header > button").click(function () {
    $("#hostname").val("");
    $("#hostip").val("");
    $("#hostuser").val("");
    $("#hostpwd").val("");
    $("#hostpwd_confirm").val("");
});
$("#appendSingleHost > div > div > div.modal-footer > button.btn.btn-secondary").click(function () {
    $("#hostname").val("");
    $("#hostip").val("");
    $("#hostuser").val("");
    $("#hostpwd").val("");
    $("#hostpwd_confirm").val("");
});
$("#appendHosts > div > div > div.modal-header > button").click(function () {
    $("#hostfile").val("");
    $("#hostfile_uploadinfo").html("");
});
$("#appendHosts > div > div > div.modal-footer > button.btn.btn-secondary").click(function () {
    $("#hostfile").val("");
    $("#hostfile_uploadinfo").html("");
});

//上传host文件
$("#hostfile").change(function () {
    var form_data = new FormData($("#hostfile_form")[0]);
    $.ajax({
        type: 'POST',
        url: "/uploadapi",
        data: form_data,
        contentType: false,
        processData: false,
        success: function (data) {
            $("#hostfile_uploadinfo").html(data);
            },
        error: function () {
            $("#hostfile_uploadinfo").html("发生异常！！");
        }
    });
});

//添加单个主机信息
function post_host() {
    data = {hostname:$("#hostname").val(),hostip:$("#hostip").val(),hostuser:$("#hostuser").val(),hostpwd:$("#hostpwd").val(),hostpwd_confirm:$("#hostpwd_confirm").val()};
    //console.log(data);
    $.ajax({
        type: "POST",
        url: "/appendSingleHost",
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify(data),
        dataType: 'html',
        success:function (data) {
            $("#appendSingleHost > div > div > div.modal-header > button").click();
            $("#alert_area").html(data);
            },
        error: function () {
            alert("发生异常！");
        }
    });
}

//通过文件批量添加主机信息
function post_hosts() {
    data = {filename:$("#hostfile").val()}
    if($("#hostfile").val() == "")
        alert("请先选择文件！");
    else{
        $.ajax({
            type: 'POST',
            url: "/appendHosts",
            contentType: 'application/json; charset=UTF-8',
            data: JSON.stringify(data),
            dataType: 'html',
            success: function (data) {
                $("#appendHosts > div > div > div.modal-header > button").click();
                $("#alert_area").html(data);
                },
            error: function () {
                alert("发生异常！");
            }
        });
    }
}
