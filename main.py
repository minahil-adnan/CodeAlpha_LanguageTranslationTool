# main.py
# Language Translation Tool - CodeAlpha Internship Project
# Author: Minahil
# Date: 2026

from googletrans import Translator
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

class LanguageTranslator:
    """Main application class for Language Translation Tool"""
    
    def __init__(self, root):
        """Initialize the application"""
        self.root = root
        self.root.title("🌍 Language Translation Tool - CodeAlpha")
        self.root.geometry("650x550")
        self.root.resizable(False, False)
        self.root.configure(bg='#1a1a2e')
        
        # Initialize translator
        self.translator = Translator()
        
        # Define supported languages (3 languages as per requirement)
        self.languages = {
            'English': 'en',
            'Urdu': 'ur',
            'Hindi': 'hi'
        }
        
        # Setup GUI
        self.setup_ui()
        
    def setup_ui(self):
        """Create the user interface"""
        
        # Title Frame
        title_frame = tk.Frame(self.root, bg='#1a1a2e')
        title_frame.pack(pady=20)
        
        # Main Title
        title = tk.Label(
            title_frame,
            text="🌍 Language Translation Tool",
            font=('Arial', 24, 'bold'),
            bg='#1a1a2e',
            fg='#e94560'
        )
        title.pack()
        
        # Subtitle
        subtitle = tk.Label(
            title_frame,
            text="CodeAlpha Internship Project",
            font=('Arial', 12),
            bg='#1a1a2e',
            fg='#b0b0b0'
        )
        subtitle.pack()
        
        # Main Frame
        main_frame = tk.Frame(self.root, bg='#16213e')
        main_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # ===== INPUT SECTION =====
        # Input Label
        input_label = tk.Label(
            main_frame,
            text="📝 Enter Text to Translate:",
            font=('Arial', 12, 'bold'),
            bg='#16213e',
            fg='white'
        )
        input_label.pack(anchor='w', pady=(10, 5))
        
        # Input Text Box
        self.input_text = scrolledtext.ScrolledText(
            main_frame,
            height=4,
            font=('Arial', 11),
            bg='#0f3460',
            fg='white',
            insertbackground='white'
        )
        self.input_text.pack(fill='x', pady=(0, 10))
        
        # ===== LANGUAGE SELECTION =====
        lang_frame = tk.Frame(main_frame, bg='#16213e')
        lang_frame.pack(fill='x', pady=10)
        
        # Source Language
        tk.Label(
            lang_frame,
            text="🔤 Source Language:",
            font=('Arial', 11, 'bold'),
            bg='#16213e',
            fg='white'
        ).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
        self.source_lang = ttk.Combobox(
            lang_frame,
            values=list(self.languages.keys()),
            state='readonly',
            width=18,
            font=('Arial', 10)
        )
        self.source_lang.set('English')
        self.source_lang.grid(row=0, column=1, padx=5, pady=5)
        
        # Target Language
        tk.Label(
            lang_frame,
            text="🎯 Target Language:",
            font=('Arial', 11, 'bold'),
            bg='#16213e',
            fg='white'
        ).grid(row=0, column=2, padx=5, pady=5, sticky='w')
        
        self.target_lang = ttk.Combobox(
            lang_frame,
            values=list(self.languages.keys()),
            state='readonly',
            width=18,
            font=('Arial', 10)
        )
        self.target_lang.set('Urdu')
        self.target_lang.grid(row=0, column=3, padx=5, pady=5)
        
        # ===== TRANSLATE BUTTON =====
        self.translate_btn = tk.Button(
            main_frame,
            text="🔄 Translate",
            font=('Arial', 14, 'bold'),
            bg='#e94560',
            fg='white',
            command=self.translate_text,
            height=1,
            cursor='hand2',
            relief='flat'
        )
        self.translate_btn.pack(fill='x', pady=10)
        
        # ===== OUTPUT SECTION =====
        # Output Label
        output_label = tk.Label(
            main_frame,
            text="📄 Translation:",
            font=('Arial', 12, 'bold'),
            bg='#16213e',
            fg='white'
        )
        output_label.pack(anchor='w', pady=(10, 5))
        
        # Output Text Box
        self.output_text = scrolledtext.ScrolledText(
            main_frame,
            height=4,
            font=('Arial', 11),
            bg='#0f3460',
            fg='#00ff88',
            insertbackground='white'
        )
        self.output_text.pack(fill='x', pady=(0, 5))
        
        # ===== COPY BUTTON =====
        button_frame = tk.Frame(main_frame, bg='#16213e')
        button_frame.pack(fill='x', pady=5)
        
        self.copy_btn = tk.Button(
            button_frame,
            text="📋 Copy Translation",
            font=('Arial', 11),
            bg='#533483',
            fg='white',
            command=self.copy_translation,
            cursor='hand2',
            relief='flat'
        )
        self.copy_btn.pack(side='left', padx=5)
        
        # Clear Button
        self.clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear All",
            font=('Arial', 11),
            bg='#e94560',
            fg='white',
            command=self.clear_all,
            cursor='hand2',
            relief='flat'
        )
        self.clear_btn.pack(side='right', padx=5)
        
        # ===== STATUS BAR =====
        self.status_label = tk.Label(
            self.root,
            text="✅ Ready to translate",
            font=('Arial', 10),
            bg='#1a1a2e',
            fg='#b0b0b0'
        )
        self.status_label.pack(side='bottom', pady=10)
        
        # ===== KEYBOARD SHORTCUT =====
        self.root.bind('<Control-Return>', lambda e: self.translate_text())
        
    def translate_text(self):
        """Translate text from source to target language"""
        
        # Get input text
        text = self.input_text.get('1.0', tk.END).strip()
        
        # Validate input
        if not text:
            messagebox.showwarning(
                "Warning",
                "Please enter some text to translate!",
                parent=self.root
            )
            self.status_label.config(text="⚠️ Please enter text")
            return
        
        # Get selected languages
        source = self.languages[self.source_lang.get()]
        target = self.languages[self.target_lang.get()]
        
        # Check if languages are same
        if source == target:
            messagebox.showinfo(
                "Information",
                "Source and target languages are the same!\nPlease select different languages.",
                parent=self.root
            )
            self.status_label.config(text="⚠️ Same language selected")
            return
        
        try:
            # Update status
            self.status_label.config(text="⏳ Translating...")
            self.translate_btn.config(state='disabled')
            self.root.update()
            
            # Perform translation
            translation = self.translator.translate(
                text,
                src=source,
                dest=target
            )
            
            # Display translation
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert('1.0', translation.text)
            
            # Update status
            self.status_label.config(
                text=f"✅ Translation complete! ({self.source_lang.get()} → {self.target_lang.get()})"
            )
            
        except Exception as e:
            # Error handling
            messagebox.showerror(
                "Translation Error",
                f"Failed to translate text!\n\nError: {str(e)}",
                parent=self.root
            )
            self.status_label.config(text="❌ Translation failed")
            
        finally:
            # Re-enable button
            self.translate_btn.config(state='normal')
    
    def copy_translation(self):
        """Copy translation to clipboard"""
        text = self.output_text.get('1.0', tk.END).strip()
        
        if text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.status_label.config(text="📋 Translation copied to clipboard!")
            
            # Show confirmation
            messagebox.showinfo(
                "Success",
                "Translation copied to clipboard!",
                parent=self.root
            )
        else:
            self.status_label.config(text="⚠️ No translation to copy")
    
    def clear_all(self):
        """Clear all text fields"""
        self.input_text.delete('1.0', tk.END)
        self.output_text.delete('1.0', tk.END)
        self.status_label.config(text="🗑️ Cleared all fields")


# ===== MAIN PROGRAM =====
if __name__ == "__main__":
    # Create the application window
    root = tk.Tk()
    
    # Set window icon (optional)
    try:
        root.iconbitmap(default='icon.ico')
    except:
        pass
    
    # Create application instance
    app = LanguageTranslator(root)
    
    # Start the application
    root.mainloop()
