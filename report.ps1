if (Test-Path "reports/allure-results") {
    Remove-Item "reports/allure-results" -Recurse -Force
    }

if (Test-Path "reports/allure-report") {
    Remove-Item "reports/allure-report" -Recurse -Force
    }

pytest
Write-Host "Тесты выполнены"
allure generate reports/allure-results --clean -o reports/allure-report
Write-Host "Отчёт сгенирирован"
allure open reports/allure-report
Write-Host "Попытка открыть отчёт"