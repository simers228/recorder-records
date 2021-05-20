$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal

    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (taskID === 'New Task') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display').removeAttr('taskID')
        } else {
            modal.find('.modal-title').text('Edit Student ' + taskID)
            $('#task-form-display').attr('taskID', taskID)
        }

        if (content) {
            modal.find('.form-control').val(content);
        } else {
            modal.find('.form-control').val('');
        }
    })

    $('#new-task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (taskID === 'New Task') {
            modal.find('.modal-title').text(taskID)
            $('#new-task-form-display').removeAttr('taskID')
        } else {
            modal.find('.modal-title').text('Edit Task ' + taskID)
            $('#new-task-form-display').attr('taskID', taskID)
        }

        if (content) {
            modal.find('.new-form-control').val(content);
        } else {
            modal.find('.new-form-control').val('');
        }
    })


    $('#submit-task').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'first_name': $('#task-modal').find('.form-control1').val(),
                'last_name': $('#task-modal').find('.form-control2').val(),
                'period': $('#task-modal').find('.form-control3').val(),
                'belt': $('#task-modal').find('.form-control4').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.state').click(function () {
        const state = $(this)
        const tID = state.data('source')

        $.ajax({
            type: 'POST',
            url: '/edit/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'status': 'succeeded'
            }),
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#new-submit-task').click(function () {
        console.log("HERE!!!!!")
        // const tID = $('#new-task-form-display').attr('taskID');
        console.log($('#new-task-modal').find('.form-control1').val())
        $.ajax({
            type: 'POST',
            url: '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'first_name': $('#new-task-modal').find('.form-control1').val(),
                'last_name': $('#new-task-modal').find('.form-control2').val(),
                'class_period': $('#new-task-modal').find('.form-control3').val(),
                'current_belt': $('#new-task-modal').find('.form-control4').val(),
                'student_teacher_id': $('#new-task-modal').find('.form-control5').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });


    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
});