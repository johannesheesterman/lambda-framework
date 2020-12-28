"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.LambdaEditorProvider = void 0;
const vscode = require("vscode");
const path = require("path");
// https://lendmeyourear.net/posts/css-only-flowcharts/
class LambdaEditorProvider {
    constructor(context) {
        this.context = context;
    }
    static register(context) {
        const provider = new LambdaEditorProvider(context);
        const providerRegistration = vscode.window.registerCustomEditorProvider(LambdaEditorProvider.viewType, provider);
        return providerRegistration;
    }
    resolveCustomTextEditor(document, webviewPanel, token) {
        return __awaiter(this, void 0, void 0, function* () {
            // Setup initial content for the webview
            webviewPanel.webview.options = {
                enableScripts: true,
            };
            webviewPanel.webview.html = this.getHtmlForWebview(webviewPanel.webview);
            function updateWebview() {
                webviewPanel.webview.postMessage({
                    type: 'update',
                    text: document.getText(),
                });
            }
            const changeDocumentSubscription = vscode.workspace.onDidChangeTextDocument(e => {
                if (e.document.uri.toString() === document.uri.toString()) {
                    updateWebview();
                }
            });
            // Make sure we get rid of the listener when our editor is closed.
            webviewPanel.onDidDispose(() => {
                changeDocumentSubscription.dispose();
            });
            // Receive message from the webview.
            // webviewPanel.webview.onDidReceiveMessage(e => {
            // 	switch (e.type) {
            // 		case 'add':
            // 			this.addNewScratch(document);
            // 			return;
            // 		case 'delete':
            // 			this.deleteScratch(document, e.id);
            // 			return;
            // 	}
            // });
            updateWebview();
        });
    }
    getHtmlForWebview(webview) {
        // // Local path to script and css for the webview
        const scriptUri = webview.asWebviewUri(vscode.Uri.file(path.join(this.context.extensionPath, 'media', 'lambda-web-editor.js')));
        // const styleResetUri = webview.asWebviewUri(vscode.Uri.file(
        // 	path.join(this.context.extensionPath, 'media', 'reset.css')
        // ));
        // const styleVSCodeUri = webview.asWebviewUri(vscode.Uri.file(
        // 	path.join(this.context.extensionPath, 'media', 'vscode.css')
        // ));
        // const styleMainUri = webview.asWebviewUri(vscode.Uri.file(
        // 	path.join(this.context.extensionPath, 'media', 'catScratch.css')
        // ));
        // // Use a nonce to whitelist which scripts can be run
        const nonce = this.getNonce();
        return `
			<!DOCTYPE html>
			<html lang="en">
			<head>
				<meta charset="UTF-8">
				<!--
				Use a content security policy to only allow loading images from https or from our extension directory,
				and only allow scripts that have a specific nonce.
				-->
                <meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src ${webview.cspSource}; style-src ${webview.cspSource}; script-src 'nonce-${nonce}';">
               
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>Lambda Editor</title>
			</head>
			<body>
                <h1>Lambda Editor (test)</h1>    
        
                <hr />
                <code id="script-content"></code>

                <script nonce="${nonce}" src="${scriptUri}"></script>
			</body>
			</html>`;
    }
    getNonce() {
        let text = '';
        const possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        for (let i = 0; i < 32; i++) {
            text += possible.charAt(Math.floor(Math.random() * possible.length));
        }
        return text;
    }
}
exports.LambdaEditorProvider = LambdaEditorProvider;
LambdaEditorProvider.viewType = 'lambda.lambdaEditor';
//# sourceMappingURL=lambdaEditor.js.map