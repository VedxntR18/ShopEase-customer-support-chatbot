import sys
import random
from colorama import Fore, Style, init
init(autoreset=True)
from intent_classifier import IntentClassifier
from ner import extract_entities
from logger import start_log, save_message

BOT_NAME = "ShopEase Bot"
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye", "q"}
SHOW_DEBUG = True

def print_banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + f"   🛒  Welcome to {BOT_NAME} — Customer Support CLI")
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + "   Ask me about: orders, returns, refunds, products, delivery")
    print(Fore.YELLOW + "   Type 'exit' anytime to quit | Type 'help' for options")
    print(Fore.CYAN + "=" * 60 + "\n")

def print_bot(message):
    print(Fore.GREEN + f"\n  🤖 {BOT_NAME}: " + Style.RESET_ALL + message + "\n")

def print_user_prompt():
    return Fore.BLUE + "  👤 You: " + Style.RESET_ALL

def print_help():
    help_text = """
  📋 I can help you with:
     1.  Order Status & Tracking
     2.  Return Requests
     3.  Refund Status
     4.  Cancel an Order
     5.  Product Complaints (damaged/wrong item)
     6.  Delivery Issues
     7.  Payment Problems
     8.  Product Information
     9.  Discounts & Coupons
     10. Warranty Claims
     11. Talk to a Human Agent
    """
    print(Fore.YELLOW + help_text)

def personalize_response(response, entities):
    order_id = entities.get("order_id")
    product  = entities.get("product")
    phone    = entities.get("phone")
    if "{order_id}" in response:
        if order_id:
            response = response.replace("{order_id}", order_id)
        else:
            response = response.replace("{order_id}", "[your order]")
    addons = []
    if order_id:
        addons.append(f"(Order detected: {order_id})")
    if product:
        addons.append(f"(Product detected: {product})")
    if phone:
        addons.append(f"(Phone noted: {phone})")
    if addons:
        response += "  " + " ".join(addons)
    return response

def main():
    print_banner()
    print(Fore.YELLOW + "  ⚙  Loading NLP models...", end="")
    classifier = IntentClassifier()
    print(Fore.GREEN + " Done! ✓\n")
    log_file = start_log()
    opening_msg = ("Hello! I'm your ShopEase customer support "
                   "assistant. How can I help you today?")
    print_bot(opening_msg)
    save_message(log_file, "Bot", opening_msg)
    while True:
        try:
            
            user_input = input(print_user_prompt()).strip()
        except (KeyboardInterrupt, EOFError):
            bye_msg = "Session interrupted. Goodbye! Have a great day! 👋"
            print_bot(bye_msg)
            save_message(log_file, "Bot", bye_msg)
            sys.exit(0)
        if not user_input:
            print(Fore.RED + "  ⚠  Please type something!\n")
            continue
        if user_input.lower() == "help":
            print_help()
            continue
        save_message(log_file, "You", user_input)
        if user_input.lower() in EXIT_COMMANDS:
            bye_msg ="Thank you for contacting ShopEase! Have a wonderful day! 👋"
            print_bot(bye_msg)
            save_message(log_file, "Bot", bye_msg)
            sys.exit(0)
        entities = extract_entities(user_input)
        intent_tag, confidence, response = classifier.classify(user_input)
        response = personalize_response(response, entities)
        if SHOW_DEBUG:
            print(Fore.MAGENTA +
                  f"  [DEBUG] Intent: {intent_tag} | Confidence: {confidence} | "
                  f"Entities: {entities}")
        print_bot(response)
        save_message(log_file, "Bot", response)

if __name__ == "__main__":
    main()