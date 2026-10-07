INTENTS = [
    {
        "tag": "greeting",
        "patterns": [
            "hello", "hi", "hey", "good morning", "good evening",
            "howdy", "what's up", "greetings", "hi there"
        ],
        "responses": [
            "Hello! Welcome to ShopEase Support. How can I help you today?",
            "Hi there! I'm your ShopEase assistant. What can I do for you?",
            "Hey! Welcome. Ask me about orders, returns, refunds, or products!"
        ]
    },
    {
        "tag": "goodbye",
        "patterns": [
            "bye", "goodbye", "see you", "take care", "quit",
            "exit", "that's all", "no more help", "thanks bye"
        ],
        "responses": [
            "Thank you for contacting ShopEase! Have a great day!",
            "Goodbye! Don't hesitate to reach out if you need help again.",
            "Take care! We're always here for you. Bye!"
        ]
    },
    {
        "tag": "order_status",
        "patterns": [
            "where is my order", "track my order", "order status",
            "has my order shipped", "when will my order arrive",
            "order not delivered", "check my order", "order tracking",
            "what is the status of my order", "my order is late"
        ],
        "responses": [
            "Please share your Order ID (format: ORD-XXXXX) and I'll look it up for you.",
            "I can help track your order! Could you provide your Order ID?",
            "Sure! Share your Order ID starting with ORD- and I'll check the status."
        ]
    },
    {
        "tag": "order_id_provided",
        "patterns": [
            "my order id is", "order number", "order id",
            "ORD-", "my order", "order details for"
        ],
        "responses": [
            "Got it! Order {order_id} is currently OUT FOR DELIVERY and will arrive by tomorrow.",
            "Order {order_id} has been SHIPPED via BlueDart. Expected delivery: 2 business days.",
            "Order {order_id} is PROCESSING at our warehouse. It will ship within 24 hours."
        ]
    },
    {
        "tag": "return_request",
        "patterns": [
            "i want to return", "how to return", "return my order",
            "return policy", "can i return", "return process",
            "want to send back", "return item", "initiate return",
            "return request"
        ],
        "responses": [
            "You can return items within 30 days of delivery. Go to My Orders → Select Order → Click 'Return'. Need help?",
            "Our return policy allows returns within 30 days. Visit the app or website to initiate. Want me to walk you through it?",
            "Sure! Returns are easy at ShopEase. Items must be unused and in original packaging. Shall I initiate one for you?"
        ]
    },
    {
        "tag": "refund_status",
        "patterns": [
            "where is my refund", "refund status", "when will i get refund",
            "refund not received", "money not returned", "refund pending",
            "how long for refund", "check refund", "refund processing"
        ],
        "responses": [
            "Refunds are processed within 5-7 business days after return pickup. Please check your bank account.",
            "Your refund is being processed! Bank transfers take 5-7 days, UPI is faster (1-2 days).",
            "Once we receive the returned item, refunds are initiated within 48 hours. Bank credit takes 5-7 days."
        ]
    },
    {
        "tag": "product_complaint",
        "patterns": [
            "received damaged product", "broken item", "wrong product received",
            "product is defective", "item is damaged", "not working",
            "product quality is bad", "received wrong item", "product complaint",
            "item broken", "defective product"
        ],
        "responses": [
            "I'm really sorry about that! We'll arrange a free replacement immediately. Please share your Order ID.",
            "That's unacceptable and I sincerely apologize. We'll send a replacement or full refund — your choice!",
            "Oh no! We're sorry for the inconvenience. We take product quality seriously. Let me escalate this right away."
        ]
    },
    {
        "tag": "delivery_issue",
        "patterns": [
            "delivery failed", "courier not found", "delivery boy problem",
            "nobody came for delivery", "missed delivery", "delivery attempt failed",
            "package not delivered", "not at home delivery", "delivery problem"
        ],
        "responses": [
            "Sorry about the missed delivery! We'll reschedule it for you. Are you available tomorrow?",
            "The courier will retry delivery within 24 hours. You can also choose a new delivery slot in the app.",
            "I've flagged this. Our delivery team will attempt redelivery tomorrow. Shall we update your address?"
        ]
    },
    {
        "tag": "cancel_order",
        "patterns": [
            "cancel my order", "i want to cancel", "stop my order",
            "don't want the order", "cancel the purchase", "abort order",
            "how to cancel", "cancel order request", "please cancel"
        ],
        "responses": [
            "Orders can be cancelled before they are shipped. Go to My Orders → Select → Cancel Order.",
            "Sure! If your order hasn't shipped yet, I can cancel it immediately. Share your Order ID!",
            "I'll help you cancel that. Note: once shipped, you'll need to use the return process instead."
        ]
    },
    {
        "tag": "payment_issue",
        "patterns": [
            "payment failed", "money deducted but order not placed",
            "transaction failed", "payment not confirmed", "charged twice",
            "double payment", "payment issue", "money debited no order"
        ],
        "responses": [
            "If money was deducted but no order was placed, it will auto-refund within 5-7 days.",
            "Payment failures are auto-reversed to your account. If not received in 7 days, contact your bank.",
            "That sounds like a failed transaction. Deducted amount will be refunded within 5-7 business days."
        ]
    },
    {
        "tag": "product_info",
        "patterns": [
            "tell me about this product", "product details", "product specifications",
            "is this product available", "product features", "product description",
            "what are the specs", "product info", "about the product"
        ],
        "responses": [
            "Could you share the product name or ID? I'll pull up the specifications for you!",
            "Sure! Please tell me the product name and I'll give you all the details.",
            "Happy to help! Share the product name and I'll describe its features and availability."
        ]
    },
    {
        "tag": "discount_coupon",
        "patterns": [
            "do you have any coupon", "discount code", "promo code",
            "any offers today", "coupon for discount", "apply coupon",
            "sale going on", "best offers", "coupon not working"
        ],
        "responses": [
            "Use code SAVE10 for 10% off on orders above ₹500! Valid this week only.",
            "Today's deals: FIRST20 (20% off for new users), FLAT100 (₹100 off above ₹999).",
            "Check the 'Offers' section in our app for real-time coupons. Code SAVE10 always works!"
        ]
    },
    {
        "tag": "contact_agent",
        "patterns": [
            "talk to human", "connect to agent", "speak to representative",
            "real person please", "customer care number", "human support",
            "live agent", "customer service contact", "escalate my issue"
        ],
        "responses": [
            "Connecting you to a live agent... Meanwhile, our helpline is 1800-XXX-XXXX (9AM-9PM).",
            "I'll escalate this to a human agent right away. You can also call 1800-XXX-XXXX.",
            "Sure! Our customer care: 1800-XXX-XXXX | Email: support@shopease.com | 9AM-9PM."
        ]
    },
    {
        "tag": "warranty",
        "patterns": [
            "warranty on product", "how long is warranty", "warranty claim",
            "product warranty", "is it under warranty", "warranty expired",
            "claim warranty", "warranty details", "warranty period"
        ],
        "responses": [
            "Most electronics come with 1-year manufacturer warranty. Check the product page for specifics.",
            "Warranty claims can be filed via My Orders → Select Product → Claim Warranty.",
            "Warranty period varies by product. Share the product name and I'll check for you!"
        ]
    },
    {
        "tag": "thank_you",
        "patterns": [
            "thank you", "thanks", "thanks a lot", "many thanks",
            "that helped", "great help", "awesome", "perfect", "wonderful"
        ],
        "responses": [
            "You're welcome! Is there anything else I can help you with?",
            "Happy to help! Let me know if you need anything else.",
            "Glad I could assist! Have a great shopping experience with ShopEase!"
        ]
    },
    {
    "tag": "frustration",
    "patterns": [
        "i hate this", "this is terrible", "worst service",
        "i am frustrated", "very disappointed", "this is awful",
        "i hate this order", "i hate this site", "so annoying",
        "this is ridiculous", "pathetic service", "bad experience"
    ],
    "responses": [
        "I'm really sorry you feel this way. We want to make this right — how can I help?",
        "I completely understand your frustration and sincerely apologize. What went wrong?",
        "I'm sorry for the bad experience. Please tell me what happened and I'll fix it immediately."
    ]
    }
]