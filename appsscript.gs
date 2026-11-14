// Google Apps Script for UK Energy Lead Capture
// Instructions: https://script.google.com → New Project → Paste this code

function doPost(e) {
  const spreadsheetId = PropertiesService.getScriptProperties().getProperty('SPREADSHEET_ID');
  if (!spreadsheetId) {
    throw new Error('SPREADSHEET_ID Script Property is not configured');
  }
  const sheet = SpreadsheetApp.openById(spreadsheetId).getSheetByName('Leads');
  if (!sheet) {
    throw new Error('Spreadsheet does not contain a Leads sheet');
  }
  
  // Parse the incoming data
  const data = JSON.parse(e.postData.contents);
  
  // Add timestamp and data to sheet
  const row = [
    new Date(),
    data.name || '',
    data.email || '',
    data.postcode || '',
    data.energyType || '',
    data.usage || '',
    data.savings || 'TBD'
  ];
  
  sheet.appendRow(row);
  
  // Send Telegram notification
  sendTelegramNotification(data);
  
  return ContentService.createTextOutput(JSON.stringify({success: true}));
}

function sendTelegramNotification(data) {
  // Keep credentials in Apps Script Project Settings > Script Properties.
  // A placeholder token used to make every notification call fail even
  // after the lead itself had been written successfully.
  const botToken = PropertiesService.getScriptProperties().getProperty('TELEGRAM_BOT_TOKEN');
  const chatId = PropertiesService.getScriptProperties().getProperty('TELEGRAM_CHAT_ID');
  if (!botToken || !chatId) {
    console.warn('Telegram notification skipped: Script Properties are not configured');
    return;
  }
  
  const message = `🔔 *New Energy Quote Request!*

*Name:* ${data.name || 'Not provided'}
*Email:* ${data.email || 'Not provided'}
*Postcode:* ${data.postcode || 'Not provided'}
*Type:* ${data.energyType || 'Not provided'}
*Usage:* £${data.usage || 'Not provided'}/year

Potential savings: £${data.savings || 'TBD'}/year`;

  const url = `https://api.telegram.org/bot${botToken}/sendMessage`;
  
  UrlFetchApp.fetch(url, {
    method: 'POST',
    contentType: 'application/json',
    payload: JSON.stringify({
      chat_id: chatId,
      text: message,
      parse_mode: 'Markdown'
    })
  });
}

// For testing - manually add a lead
function testLead() {
  const testData = {
    name: 'Test User',
    email: 'test@example.com',
    postcode: 'SW1A 1AA',
    energyType: 'dual',
    usage: '4200',
    savings: '220'
  };
  
  sendTelegramNotification(testData);
}
