// ocr.swift — macOS Vision OCR 自检：无文字输出 NO_TEXT_DETECTED（exit 0），
// 检出文字输出明细（exit 1），错误 exit 2。
import Foundation
import Vision
import AppKit

let args = CommandLine.arguments
guard args.count >= 2 else { fputs("usage: ocr <image>\n", stderr); exit(2) }
let path = args[1]
guard let img = NSImage(contentsOfFile: path),
      let tiff = img.tiffRepresentation,
      let rep = NSBitmapImageRep(data: tiff),
      let cg = rep.cgImage else { fputs("LOAD_FAILED\n", stderr); exit(2) }

let req = VNRecognizeTextRequest()
req.recognitionLevel = .accurate
req.usesLanguageCorrection = true
req.recognitionLanguages = ["ja-JP", "zh-Hans", "zh-Hant", "en-US"]

let handler = VNImageRequestHandler(cgImage: cg, options: [:])
do {
    try handler.perform([req])
    let results = req.results ?? []
    if results.isEmpty {
        print("NO_TEXT_DETECTED")
        exit(0)
    }
    print("TEXT_DETECTED \(results.count)")
    for r in results.prefix(12) {
        if let t = r.topCandidates(1).first {
            let bb = r.boundingBox
            print(String(format: "  > \"%@\" conf=%.2f bb=(%.2f,%.2f,%.2f,%.2f)",
                         t.string, t.confidence, bb.origin.x, bb.origin.y, bb.width, bb.height))
        }
    }
    exit(1)
} catch {
    fputs("OCR_ERROR \(error)\n", stderr)
    exit(2)
}
