# Directory to search
$baseDir = "C:\Users\rafa\OneDrive\Documentos\GitHub\1-Ciberseguridad\rm.ps1"

# Search and delete files containing #Index
Get-ChildItem -Path $baseDir -Recurse -File -Filter *.md | ForEach-Object {
    $content = Get-Content -Path $_.FullName
    if ($content -match "#Index") {
        Write-Host "Deleting file:" $_.FullName
        Remove-Item -Path $_.FullName -Force
    }
}

Write-Host "Operation complete."
