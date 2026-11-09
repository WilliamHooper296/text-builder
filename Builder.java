import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Random;

public class Builder{

    private final Random random = new Random();

    HashMap<List<String>, HashMap<String, Integer>> build(Path filepath, int order){
        HashMap<List<String>, HashMap<String, Integer>> backing = new HashMap<>();

        try(BufferedReader br = new BufferedReader(Files.newBufferedReader(filepath))){

            int count = 0;
            String line = "";
            String[] prevWords = new String[order];
            while((line = br.readLine()) != null){
                String[] words = line.split("\\s+");

                for(String word: words){
                    if(count < order){
                        prevWords[count] = word;
                        count++;
                        continue;
                    }

                    backing.computeIfAbsent(List.of(prevWords), k -> new HashMap<>()).merge(word, 1, Integer::sum);

                    for(int i = 0; i < order-1; i++){
                        prevWords[i] = prevWords[i+1];
                    }
                    prevWords[order-1] = word;

                }
            }
        }catch(Exception e){
            System.out.println("Exception Caught: " + e);
        }

        return backing;
    }

    void read(HashMap<List<String>, HashMap<String, Integer>> backing, int words){

        List<List<String>> keys = new ArrayList<>(backing.keySet());

        List<String> prevWords = new ArrayList<>(keys.get(random.nextInt(keys.size())));

        for(int i = 0; i < words; i++){
            String word = nextWord(backing, prevWords);
            System.out.print(word + " ");
            System.out.flush();
            prevWords.remove(0);
            prevWords.add(word);
            try{
                Thread.sleep(10);
            }catch(Exception e){System.out.println("Error: " + e);}
        }

    }

    private String nextWord(HashMap<List<String>, HashMap<String, Integer>> backing, List<String> key){

        HashMap<String, Integer> options = backing.get(key);

        if(options == null || options.isEmpty()){
            List<List<String>> keys = new ArrayList<>(backing.keySet());
            List<String> prevWords = keys.get(random.nextInt(keys.size()));
            options = backing.get(prevWords);
        }

        int total = 0;
        for(int option: options.values()){
            total += option;
        }

        int index = random.nextInt(total);

        for(Map.Entry<String, Integer> entry : options.entrySet()){
            index -= entry.getValue();

            if(index < 0){
                return entry.getKey();
            }
        }

        return null;

    }

}