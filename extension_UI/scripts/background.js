// background.js

// Create a context menu item for text selection
chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
      id: "sampleContextMenu",
      title: "Sticky Note",
      contexts: ["selection"]
    });
});
  
// Add a click event listener for the context menu
chrome.contextMenus.onClicked.addListener((info, tab) => {
if (info.menuItemId === "sampleContextMenu" && info.selectionText) {
    // Execute the hello.js script in the current tab
    chrome.scripting.executeScript({
    target: {tabId: tab.id},
    files: ['scripts\/save_message.js']
    });
}
});
  
  