(function() {

    const vscode = acquireVsCodeApi();

    const contentDiv = document.getElementById('script-content');

    function updateContent(/** @type {string} */ text) {
		contentDiv.innerText = text;
	}

    window.addEventListener('message', event => {
		const message = event.data; // The json data that the extension sent
		switch (message.type) {
			case 'update':
				const text = message.text;
				updateContent(text);
				vscode.setState({ text });
				return;
		}
    });

    const state = vscode.getState();
	if (state) {
		updateContent(state.text);
	}    

})();