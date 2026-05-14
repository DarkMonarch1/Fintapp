# Fintapp

<p align="center">
  <img src="src/main/resources/images/logo.png" width="200" alt="Fintapp logo">
</p>

<p align="center">
Fintapp is a simulated Mobile Financial System (MFS) desktop application built with JavaFX. It mirrors the original course-project feature set: registration and login, dashboard shortcuts, add money, payments, send money, mobile top-up, transfers to bank, bill pay, ticket booking (webview), calculators, transaction history, limits, and withdraw locations. User data and transactions are stored under <code>%USERPROFILE%\Fintapp\data</code> on Windows (or <code>~/Fintapp/data</code> elsewhere).
</p>

## Build and run (Maven)

Requires **JDK 21** and **Maven**. Open the folder that contains **`pom.xml`** (the inner `lenden-mfs-cse215-main` directory if your zip has two nested folders).

**Why `mvn javafx:run` can fail:** Maven only auto-resolves short plugin prefixes like `javafx:` for a few default groups (`org.apache.maven.plugins`, `codehaus.mojo`). The OpenJFX plugin lives under **`org.openjfx`**, so use the **full plugin coordinates** (or `exec:java` below).

Run the desktop app (recommended):

```bash
mvn org.openjfx:javafx-maven-plugin:0.0.8:run
```

Alternative (uses the `exec` prefix from the default plugin group):

```bash
mvn exec:java
```

On Windows PowerShell, if `-D` flags get mangled, prefer the two commands above without extra `-D` arguments.

Compile only:

```bash
mvn -q compile
```

## Features

- User registration and login  
- Account summary and my account  
- Add money (bank / card)  
- Make payment, send money, mobile top-up  
- Fintapp to bank transfer  
- Pay bills, withdraw cash, withdraw locations map  
- Book tickets (external sites in WebView)  
- Basic, percentage, and interest calculators  
- Transaction history and daily limits  

## Project layout

- `src/main/java/com/fintapp` — application code (`Main`, controllers, models, services)  
- `src/main/resources/fxml` — screens  
- `src/main/resources/css` — styles  
- `src/main/resources/images` — logos, icons, dashboard tiles  
- `pom.xml` — JavaFX + FontAwesomeFX dependencies  

