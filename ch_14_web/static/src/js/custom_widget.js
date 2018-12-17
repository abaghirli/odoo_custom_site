odoo.define('ch_14_web', function(require)
{
    var core = require('web.core'),
        form_common = require('web.form_common');
    var FieldMany2OneButtons = form_common.AbstractField.extend({
            class_name: 'oe_form_field_many2one_buttons',
            init: Function()
            {
                var result = this._super.apply(this, arguments);
                   this.user_list = {
                       1: {
                           name: 'Administrator',
                          },
                       4: {
                           name: 'Demo user',
                          },
                   };
                this.on(
                   'change:effective_readonly', this,
                   this.effective_readonly_changed)
                return result;
            },
            events: {
                'click .btn': 'button_clicked',
            }
        })

})