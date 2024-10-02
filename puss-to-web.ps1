# PowerShell Script to Ask for Publishing Latest Version

# Ask the user if they want to publish the latest version
$publish = Read-Host "Do you want to publish the latest version? (yes/no)"

# Check the user's input
if ($publish -eq "yes") {
    # Execute npx quartz sync
    Write-Host "indexing files..."
    Set-Location C:\Users\rafa\OneDrive\Documentos\GitHub\quartz\content\
    python indexer.py
    Write-Host "Publishing latest version..."
    Set-Location C:\Users\rafa\OneDrive\Documentos\GitHub\quartz\
    npx quartz sync
    git push
} else {
    Write-Host "Publishing cancelled."
}
