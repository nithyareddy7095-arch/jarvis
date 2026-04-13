class ChatReply {
  final String answer;
  final List<String> tips;
  final String stage;

  ChatReply({required this.answer, required this.tips, required this.stage});

  factory ChatReply.fromJson(Map<String, dynamic> json) {
    return ChatReply(
      answer: json['answer'] ?? '',
      tips: (json['tips'] as List<dynamic>? ?? []).map((e) => e.toString()).toList(),
      stage: json['stage'] ?? 'Seed',
    );
  }
}

class MarketPrice {
  final String crop;
  final String market;
  final double conventionalPrice;
  final double organicPrice;
  final String demandTrend;

  MarketPrice({
    required this.crop,
    required this.market,
    required this.conventionalPrice,
    required this.organicPrice,
    required this.demandTrend,
  });

  factory MarketPrice.fromJson(Map<String, dynamic> json) {
    return MarketPrice(
      crop: json['crop'] ?? '',
      market: json['market'] ?? '',
      conventionalPrice: (json['conventional_price'] ?? 0).toDouble(),
      organicPrice: (json['organic_price'] ?? 0).toDouble(),
      demandTrend: json['demand_trend'] ?? '',
    );
  }
}
