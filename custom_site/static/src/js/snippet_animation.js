odoo.define('custom_site.snippets_animation', function(require)
{
    "use strict";
    var animation = require('web_editor.snippets.animation'),
        Model = require('web.Model');

    animation.registry.channel_snippet = animation.Class.extend({
    selector: ".channel_snippet",
    start: function()
        {
            var self = this,
                number = 3;
                _.each(this.$el.attr('class').split(/\s+/),
                function(cls){
                    if(cls.indexOf('channel_snippet-show') == 0)
                    {
                        number = parseInt(
                            cls.substring('channel_snippet-show'.length));
                    }
                });
                this.$el.find('td').parents('tr').remove();
                new Model('mail.channel').call('search_read', [], {
                    domain: [],
                    fields: ['name', 'create_date'],
                    order: 'create_date desc',
                    limit: number,
                }).then(function(data){
                    var $table = self.$el.find('table');
                    _.each(data, function(channel){
                        $table.append(
                            jQuery('<tr />').append(
                                jQuery('<td />').text(channel.name),
                                jQuery('<td />').text(channel.create_date)
                            )
                        );
                    })
                });
        },
    });
});