import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [progress, setProgress] = useState(0);
  const [improvedText, setImprovedText] = useState('');
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!selectedFile) {
      alert("Por favor, selecciona un archivo PDF.");
      return;
    }
    setLoading(true);
    setProgress(0);
    const formData = new FormData();
    formData.append('cv', selectedFile);

    const progressInterval = setInterval(() => {
      setProgress((prev) => {
        if (prev < 80) return prev + Math.floor(Math.random() * 10) + 5;
        return prev;
      });
    }, 500);

    try {
      // Mientras pruebas localmente, la URL apunta al back-end en Cloud Run o local.
      // Para pruebas locales, usa: http://127.0.0.1:5000/process
      const response = await axios.post('http://127.0.0.1:5000/process', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        onUploadProgress: (progressEvent) => {
          const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
          setProgress(percentCompleted);
        },
      });
      clearInterval(progressInterval);
      setProgress(100);
      setImprovedText(response.data.improved_text);
    } catch (error) {
      clearInterval(progressInterval);
      console.error("Error durante el procesamiento del CV:", error);
      alert("Error durante el procesamiento del CV.");
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/download', { improved_text: improvedText }, {
        responseType: 'blob'
      });
      const url = window.URL.createObjectURL(new Blob([response.data], { type: 'application/pdf' }));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'CV_optimizado.pdf');
      document.body.appendChild(link);
      link.click();
    } catch (error) {
      console.error("Error al descargar el PDF:", error);
      alert("Error al descargar el PDF.");
    }
  };

  return (
    <div className="App">
      <header className="site-header">
        <h1>Optimiza tu CV</h1>
        <p className="motivational">
          ¡Da el salto a tu próximo empleo! Confía en nuestra herramienta para transformar tu currículum.
        </p>
      </header>
      <main className="container">
        {!improvedText && (
          <form onSubmit={handleUpload} className="upload-form">
            <input type="file" accept="application/pdf" onChange={handleFileChange} />
            <button type="submit" disabled={loading}>
              {loading ? `Procesando... ${progress}%` : "Subir y Optimizar"}
            </button>
          </form>
        )}
        {loading && (
          <div className="progress-container">
            <progress value={progress} max="100"></progress>
            <p>{progress}%</p>
          </div>
        )}
        {improvedText && (
          <div className="result-preview">
            <h2>CV Optimizado</h2>
            <textarea readOnly value={improvedText} rows="10"></textarea>
            <button onClick={handleDownload}>Descargar PDF</button>
          </div>
        )}
      </main>
      <footer className="site-footer">
        <p>&copy; 2025 Optimiza tu CV. Protegemos tus datos y garantizamos tu privacidad.</p>
      </footer>
    </div>
  );
}

export default App;
