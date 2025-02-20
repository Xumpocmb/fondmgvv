tinymce.PluginManager.add('customlink', function(editor, url) {
    editor.ui.registry.addButton('customlink', {
        text: 'Custom Link',
        onAction: function() {
            editor.windowManager.open({
                title: 'Insert Custom Link',
                body: {
                    type: 'panel',
                    items: [
                        {
                            type: 'input',
                            name: 'url',
                            label: 'URL'
                        },
                        {
                            type: 'input',
                            name: 'text',
                            label: 'Link Text'
                        }
                    ]
                },
                onSubmit: function(api) {
                    const data = api.getData();
                    editor.insertContent('<a href="' + data.url + '">' + data.text + '</a>');
                    api.close();
                }
            });
        }
    });
});
